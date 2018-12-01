let imageIndex = 0;
let images = [];
let nImages = document.getElementById("imageSlideshow").childNodes;

for (let i=0; i<nImages.length; i++) {
    let nImage = nImages[i];

    if (nImage.tagName == "IMG") {
        images.push(nImage)
    }
}

function showImage(imageIndex) {
    for (let i=0; i<images.length; i++) {
        images[i].className = "product-detail-image product-detail-image-hidden"
    }

    images[imageIndex].className = "product-detail-image"
}

function nextImage() {
    imageIndex++;

    if (imageIndex >= images.length) {
        imageIndex = 0;
    }

    showImage(imageIndex);
}

setInterval(nextImage, 5000);
