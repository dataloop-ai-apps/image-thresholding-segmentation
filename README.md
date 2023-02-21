# Image Thresholding Segmentation App

![Original image](assets/palm_tree.jpeg)
![Thresholding mask](assets/palm_tree_thresholding.jpg)

## Description

This app is a simple example of a Python application that can be published and installed in the Dataloop platform.
The components of this app are:

1. A Python function to create a Segmentation annotation using opencv thresholding function
2. A toolbar on the item menu (right-click in the data browser) to run the function
3. A toolbar in the item studio (icon in the left panel) to run the function on the active item

## Publish to App Store

To pack and publish your app to the App Store, run the following command:

```
dlp app publish --project-name <PROJECT_NAME>
```

When the app is published, you will receive a DPK ID. This ID is used to install the app into a project.

## Install App in a Project

To install a published app into a project for use, run the following command:

```
dlp app install --dpk-id <DPK ID> --project-name <PROJECT_NAME>
```

## Tutorial and How-To

To run this function, go to the dataset browser and right-click on an image. You will see a menu item called "Create
Thresholding Mask". Click on it and a new segmentation annotation will be created.

Alternatively, you can open the item annotation browser and click on the plus (+) icon in the left panel. This will run
the function on the active item.

## App Components

### Function

* make_mask

### Toolbar

* itemMenu
* itemStudio

## Environment, Docker and system requirements

This app requires only an OpenCV installation, so a specialized docker image is not required. We can use Dataloop's
default docker image.

## Contributions, Bugs and Issues - How to Contribute

Anyone is welcome to help us improve this app. [Here](CONTRIBUTING.md) are detailed instructions to help you open a bug or submit a feature request.
