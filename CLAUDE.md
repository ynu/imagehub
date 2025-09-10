# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an image repository that contains diagram files, primarily in Draw.io format and their exported PNG/SVG versions. The repository includes network architecture diagrams and other technical illustrations.

## File Types

- `.drawio` - Draw.io diagram source files
- `.drawio.svg` - SVG exports from Draw.io
- `.png` - PNG image files
- `.xml` - XML data files

## Common Operations

Since this is an image repository with diagram files, common operations would involve:

1. Opening `.drawio` files with Draw.io or diagrams.net to edit diagrams
2. Exporting diagrams to different formats (PNG, SVG) as needed
3. Version controlling diagram changes

## Development Commands

There are no manual build scripts in this repository as it's purely for storing image assets. However, there are automated GitHub Actions:

1. **Generate Draw.io Images**: Automatically generates PNG, JPG, and SVG files from Draw.io source files on commit
2. **Sync to rustfs Storage**: Automatically syncs generated files to the rustfs storage bucket

To work with these diagrams locally:
1. Open `.drawio` files directly in https://draw.io or the desktop app
2. Make changes and commit to the repository
3. GitHub Actions will automatically generate and sync the corresponding image files

## GitHub Actions

### Generate Draw.io Images
- Triggered on push events when `.drawio` files are modified
- Automatically generates PNG, JPG, and SVG files from Draw.io source files
- Removes orphaned image files when corresponding Draw.io files are deleted

### Sync to rustfs Storage
- Triggered after successful completion of the Generate Draw.io Images workflow
- Syncs all Draw.io files and their generated images to the rustfs storage bucket
- Requires secrets configuration in the repository settings

#### Authentication
The workflow uses AWS S3-compatible authentication with boto3:

You must set these secrets in your GitHub repository:
- `RUSTFS_ENDPOINT`: The base URL of your rustfs service (e.g., http://12.34.56.78:9000)
- `RUSTFS_ACCESS_KEY`: Your rustfs access key
- `RUSTFS_SECRET_KEY`: Your rustfs secret key
- `RUSTFS_BUCKET`: The bucket name (defaults to "itc")

## Architecture

This repository has a flat structure with no complex architecture. Files are organized at the root level with descriptive names indicating their content.