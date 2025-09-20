document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('upload-form');
    const imageFile = document.getElementById('image-file');
    const imagePreview = document.getElementById('image-preview');
    const resultText = document.getElementById('result-text');
    const confidenceText = document.getElementById('confidence-text');
    const loader = document.getElementById('loader');

    imageFile.addEventListener('change', () => {
        const file = imageFile.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.innerHTML = `<img src="${e.target.result}" alt="Image preview"/>`;
            };
            reader.readAsDataURL(file);
        }
        resultText.textContent = '';
        confidenceText.textContent = '';
    });

    uploadForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        if (!imageFile.files.length) {
            alert('Please choose an image file first.');
            return;
        }

        const formData = new FormData();
        formData.append('file', imageFile.files[0]);

        loader.style.display = 'block';
        resultText.textContent = '';
        confidenceText.textContent = '';

        try {
            const response = await fetch('/predict', { method: 'POST', body: formData });
            const data = await response.json();

            if (data.prediction) {
                resultText.textContent = `Prediction: ${data.prediction}`;
                confidenceText.textContent = `Confidence: ${data.confidence}`;
            } else {
                throw new Error(data.error || 'Unknown error occurred.');
            }
        } catch (error) {
            console.error('Error:', error);
            resultText.textContent = `Error: ${error.message}`;
        } finally {
            loader.style.display = 'none';
        }
    });
});