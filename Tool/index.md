---
layout: notes
---

# Tools

## ★ Game Proposal Converter
Origin version from [摩訶聖 StM4H4](https://stm4h4.com/downloads/)

<button class="download-template" data-path="proposal/proposal.md">Download proposal.md template</button>
<button class="uploadAndPreviewButton" data-target-iframe="gameProposalPreview" data-path="proposal/proposal.html.txt">Upload proposal.md</button>
<button class="downloadHtmlButton" data-for="gameProposalPreview" data-default-name="proposal.html">Download proposal.html</button>
<iframe id="gameProposalPreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

## ★ Game Outline Converter
Origin version from [摩訶聖 StM4H4](https://stm4h4.com/downloads/)

<button class="download-template" data-path="outline/outline.md">Download Outline.md template</button>
<button class="uploadAndPreviewButton" data-target-iframe="gameOutlinePreview" data-path="outline/outline.html.txt">Upload Outline.md</button>
<button class="downloadHtmlButton" data-for="gameOutlinePreview" data-default-name="outline.html">Download Outline.html</button>
<iframe id="gameOutlinePreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

## ★ Character Card, Basic ver Converter
Origin version from [摩訶聖 StM4H4](https://stm4h4.com/downloads/)

<button class="download-template" data-path="character/basic.md">Download Char_Basic.md template</button>
<button class="uploadAndPreviewButton" data-target-iframe="Char_BasicPreview" data-path="character/basic.html.txt">Upload Char_Basic.md</button>
<button class="downloadHtmlButton" data-for="Char_BasicPreview" data-default-name="basic.html">Download Char_Basic.html</button>
<iframe id="Char_BasicPreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

## ★ Character Card, Advance ver Converter
Origin version from [摩訶聖 StM4H4](https://stm4h4.com/downloads/)

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
    // Split the Markdown content into lines for parsing
    const lines = mdContent.split('\n');

    // Initialize an object to hold the parsed content by tags
    const contentByTag = {};

    // Parse each line of the Markdown content
    lines.forEach(line => {
        // Check if the line is a heading, indicating a new section/tag
        if (line.startsWith("##")) {
            const tag = line.substring(2).trim();
            // Ensure an array exists for this tag to hold its content
            if (!contentByTag[tag]) {
                contentByTag[tag] = [];
            }
        } else if (line.startsWith("*")) {
            // Assuming the last tag encountered is the current section
            const lastTag = Object.keys(contentByTag).pop();
            // Add list item content to the current tag's array, formatted as HTML
            if (lastTag) {
                contentByTag[lastTag].push(line.substring(1).trim() + "<br>");
            }
        } else {
            // For non-list content, add it directly to the last encountered tag's array
            const lastTag = Object.keys(contentByTag).pop();
            if (lastTag) {
                contentByTag[lastTag].push(line.trim());
            }
        }
    });

    // Convert the arrays of content into HTML strings
    Object.keys(contentByTag).forEach(tag => {
        contentByTag[tag] = contentByTag[tag].join(' ');
    });

    // Load the template HTML and replace placeholders with actual content
    let htmlOutput = templateHtml;
    Object.entries(contentByTag).forEach(([tag, content]) => {
        // Create a regex to find the placeholder in the HTML template
        const regex = new RegExp(`\\{\\{${tag}\\}\\}`, 'g');
        // Replace the placeholder with the actual content
        htmlOutput = htmlOutput.replace(regex, content);
    });

    // Return the modified HTML, ready for display or download
    return htmlOutput;
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
