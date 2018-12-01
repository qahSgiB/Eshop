let imageSlideShowIndex = 0;

let images = [];
let nImages = document.getElementById("imageSlideshow").childNodes;
for (let i=0; i<nImages.length; i++) {
    let nImage = nImages[i];

    if (nImage.tagName == "IMG") {
        images.push(nImage)
    }
}

let imageSelectors = []
let nImageSelectors = document.getElementById("imageSlection").childNodes;
for (let i=0; i<nImageSelectors.length; i++) {
    let nImageSelector = nImageSelectors[i].childNodes;

    for (let j=0; j<nImageSelector.length; j++) {
        let nnImageSelector = nImageSelector[j];

        if (nnImageSelector.tagName == "INPUT") {
            imageSelectors.push(nnImageSelector);
        }
    }
}

for (let i=0; i<imageSelectors.length ; i++) {
    imageSelectors[i].addEventListener("click", () => {showImage(i)})
}

function showImage(imageIndex) {
    for (let i=0; i<images.length; i++) {
        images[i].className = "product-detail-image product-detail-image-hidden"
    }

    images[imageIndex].className = "product-detail-image";

    imageSelectors[imageIndex].checked = true;
}

function nextImage() {
    imageSlideShowIndex++;

    if (imageSlideShowIndex >= images.length) {
        imageSlideShowIndex = 0;
    }

    showImage(imageSlideShowIndex);
}

// setInterval(nextImage, 5000);
showImage(0);
