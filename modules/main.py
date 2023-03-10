import dtlpy as dl


@dl.Package.defs.module()
class GrayMaskService(dl.BaseServiceRunner):
    @dl.Package.defs.function(inputs={'item': dl.Item, 'threshold': int, 'label': str})
    def make_mask(self, item, threshold=100, label='mask'):
        import numpy as np
        from PIL import Image

        buffer = item.download(save_locally=False)
        img = np.asarray(Image.open(buffer).convert('L'))

        assert len(img.shape) < 3, "Image must be grayscale"

        img = img.copy()
        mask = img < threshold
        # img[mask] = 255
        # img[~mask] = 0
        # plt.imshow(img, cmap='gray')

        builder = item.annotations.builder()
        builder.add(annotation_definition=dl.Segmentation(geo=mask,
                                                          label=label))
        item.annotations.upload(annotations=builder)

    @dl.Package.defs.function(inputs={'item': dl.Item, 'label': str})
    def binary_threshold_mask(self, item, threshold=100, label='dark'):
        import cv2
        import numpy as np

        buffer = item.download(save_locally=False)
        img = cv2.imdecode(np.frombuffer(buffer.read(), np.uint8), cv2.IMREAD_GRAYSCALE)

        assert len(img.shape) < 3, "Image must be grayscale"

        img = img.copy()
        ret, mask = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV)

        # import matplotlib.pyplot as plt
        # plt.imshow(mask, cmap='gray')
        # plt.show()

        builder = item.annotations.builder()
        builder.add(annotation_definition=dl.Segmentation(geo=mask,
                                                          label=label))
        item.annotations.upload(annotations=builder)
