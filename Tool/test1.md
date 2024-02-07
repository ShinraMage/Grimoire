---
layout: notes
---

# Tools

## ★ Game Proposal Converter
<button class="download-template" data-path="proposal/proposal.md">Download proposal.md template</button>
<button class="uploadAndPreviewButton" data-target-iframe="gameProposalPreview" data-path="proposal/proposal.html.txt">Upload proposal.md</button>
<button class="downloadHtmlButton" data-for="gameProposalPreview" data-default-name="proposal.html">Download proposal.html</button>
<iframe id="gameProposalPreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

## ★ Game Outline Converter
<button class="download-template" data-path="outline/outline.md">Download Outline.md template</button>
<button class="uploadAndPreviewButton" data-target-iframe="gameOutlinePreview" data-path="outline/outline.html.txt">Upload Outline.md</button>
<button class="downloadHtmlButton" data-for="gameOutlinePreview" data-default-name="outline.html">Download Outline.html</button>
<iframe id="gameOutlinePreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

## ★ Character Card, Basic ver Converter
<button class="download-template" data-path="character/basic.md">Download Char_Basic.md template</button>
<button class="uploadAndPreviewButton" data-target-iframe="Char_BasicPreview" data-path="character/basic.html.txt">Upload Char_Basic.md</button>
<button class="downloadHtmlButton" data-for="Char_BasicPreview" data-default-name="basic.html">Download Char_Basic.html</button>
<iframe id="Char_BasicPreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

## ★ Character Card, Advance ver Converter
<button class="download-template" data-path="character/advance.md">Download Char_Advance.md template</button>
<button class="uploadAndPreviewButton" data-target-iframe="Char_AdvancePreview" data-path="character/advance.html.txt">Upload Char_Advance.md</button>
<button class="downloadHtmlButton" data-for="Char_AdvancePreview" data-default-name="advance.html">Download Char_Advance.html</button>
<iframe id="Char_AdvancePreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

<script>
document.querySelectorAll('.download-template').forEach(button => {
    button.addEventListener('click', function() {
        const filePath = this.getAttribute('data-path');
        const link = document.createElement('a');
        link.href = './' + filePath;
        link.download = filePath.substring(filePath.lastIndexOf('/') + 1);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    });
});

document.querySelectorAll('.uploadAndPreviewButton').forEach(button => {
    button.addEventListener('click', function() {
        const targetIframeID = this.getAttribute('data-target-iframe');
        const htmlFilePath = this.getAttribute('data-path');
        const fileInput = document.createElement('input');
        fileInput.type = 'file';
        fileInput.accept = '.md';
        
        fileInput.onchange = e => {
            const file = e.target.files[0];
            if (!file) return;
            
            const reader = new FileReader();
            reader.onload = function(e) {
                const mdContent = e.target.result;
                
                fetch('./' + htmlFilePath)
                    .then(response => response.text())
                    .then(templateHtml => {
                        const convertedHtml = convertMdContentToHtml(mdContent, templateHtml);
                        displayInIframe(convertedHtml, targetIframeID);
                        prepareDownloadHtmlButton(convertedHtml, button.nextElementSibling, targetIframeID);
                    })
                    .catch(error => console.error('Error loading the HTML template:', error));
            };
            
            reader.readAsText(file);
        };

        fileInput.click();
    });
});

function convertMdContentToHtml(mdContent, templateHtml) {
    // Placeholder for conversion logic
    // Implement the actual conversion logic based on your specific needs here.
    // This is a simplified example that directly returns the templateHtml.
    return templateHtml; // Replace with actual conversion logic
}

function displayInIframe(htmlContent, iframeId) {
    const targetIframe = document.getElementById(iframeId);
    const blob = new Blob([htmlContent], {type: 'text/html'});
    const url = URL.createObjectURL(blob);
    targetIframe.src = url;
}

function prepareDownloadHtmlButton(htmlContent, downloadButton, iframeId) {
    const defaultName = downloadButton.getAttribute('data-default-name');
    downloadButton.onclick = () => {
        const blob = new Blob([htmlContent], {type: 'text/html'});
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = defaultName;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };
}
</script>
