---
layout: notes
---

# Tools

## Converter 
([python ver](https://github.com/posetmage/GameDesign/blob/master/Tool/convert.py))

```
upload md file Use ## as content and replace {{}} in html
```


<button class="upload-template" data-target-iframe="OutPreview">Upload template.html</button>
<button class="upload-markdown" data-target-iframe="OutPreview">Upload .md</button>
<button class="download-result" data-for="OutPreview">outcome.html</button>
<iframe id="OutPreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

<script>
document.querySelector('.upload-template').addEventListener('click', function() {
    const targetIframeID = this.getAttribute('data-target-iframe');
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = '.html';
    
    fileInput.onchange = e => {
        const file = e.target.files[0];
        if (!file) return;
        
        const reader = new FileReader();
        reader.onload = function(e) {
            templateHtmlContent = e.target.result;
            displayInIframe(templateHtmlContent, targetIframeID); // Display uploaded template in iframe
        };
        
        reader.readAsText(file);
    };

    fileInput.click();
});

document.querySelector('.upload-markdown').addEventListener('click', function() {
    const targetIframeID = this.getAttribute('data-target-iframe');
    if (!templateHtmlContent) {
        alert("Please upload a template.html first.");
        return;
    }
    
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = '.md';
    
    fileInput.onchange = e => {
        const file = e.target.files[0];
        if (!file) return;
        
        const reader = new FileReader();
        reader.onload = function(e) {
            const mdContent = e.target.result;
            const convertedHtml = convertMdContentToHtml(mdContent, templateHtmlContent);
            displayInIframe(convertedHtml, targetIframeID); // Update iframe with merged content
        };
        
        reader.readAsText(file);
    };

    fileInput.click();
});

document.querySelector('.download-result').addEventListener('click', function() {
    const iframeId = this.getAttribute('data-for');
    const iframeContent = document.getElementById(iframeId).contentDocument.documentElement.outerHTML;
    const blob = new Blob([iframeContent], {type: 'text/html'});
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'outcome.html';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
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
</script>

### examples
#### Save the Cat Beatsheet
* [beatsheet.html template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/outline/Beat%20Sheet.html)
* [beatsheet.md template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/outline/Beat%20Sheet.md)
* You can use [GPTs - Navi](https://chat.openai.com/g/g-NsZTxNrJJ) to gen this beatsheet.md

#### tables from [摩訶聖 StM4H4](https://stm4h4.com/downloads/)
* Proposal
  * [proposal.md template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/proposal/proposal.md)
  * [proposal.html template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/proposal/proposal.html)
  * You can use [GPTs - Vixen](https://chat.openai.com/g/g-oR0tADta6) to gen proposal.md 
* Outline
  * [Outline.md template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/outline/outline.md)
  * [Outline.html template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/outline/outline.html)
* Character Card
  * [Character.md template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/character/character.md)
  * [Char_Basic.html template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/character/basic.html)
  * [Char_Advance.html template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/character/advance.html)
  * You can use [GPTs - Scarlett](https://chat.openai.com/g/g-LD06QK4Bt) to gen Character.md 
