# MarkItDown Codespace base image
# Installs MarkItDown at build time so it is cached in the prebuild
# and available instantly to everyone who opens a codespace.
FROM mcr.microsoft.com/devcontainers/python:3.12

# Optional system packages used by some MarkItDown converters
# (ffmpeg = audio transcription, libgl/poppler = image & PDF handling).
# Comment out if you only need core Office/PDF conversion to keep the image lean.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ffmpeg \
        poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Install MarkItDown with all optional format extras.
# For a lighter image, replace 'markitdown[all]' with 'markitdown'
# plus only the extras you need, e.g. 'markitdown[pdf,docx,pptx,xlsx]'.
RUN pip install --no-cache-dir 'markitdown[all]'

# Quick sanity check at build time (fails the build if install is broken).
RUN markitdown --version
