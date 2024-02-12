---
layout: notes
---

# Tools

## Converter
{% raw %}
```
upload md file Use ## as content and replace {{}} in html
```
{% endraw %}


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

#### [python ver](https://github.com/posetmage/GameDesign/blob/master/Tool/convert.py)

https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/proposal/proposal.html

#### examples
Origin version from [摩訶聖 StM4H4](https://stm4h4.com/downloads/)
* Proposal
  * <button class="download-template" data-path="https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/proposal/proposal.md">proposal.md template</button>
  * <button class="download-template" data-path="https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/proposal/proposal.html">proposal.html template</button>
* Outline
  * <button class="download-template" data-path="https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/outline/outline.md">Outline.md template</button>
  * <button class="download-template" data-path="https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/outline/outline.html">Outline.html template</button>
* Basic Character Card
  * <button class="download-template" data-path="https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/character/basic.md">Char_Basic.md template</button>
  * <button class="download-template" data-path="https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/character/basic.html">Char_Basic.html template</button>
* Advance Character Card
  * <button class="download-template" data-path="https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/character/advance.md">Char_Advance.md template</button>
  * <button class="download-template" data-path="https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/character/advance.html">Char_Advance.html template</button>


<script>
document.querySelectorAll('.download-template').forEach(button => {
    button.addEventListener('click', function() {
        const filePath = this.getAttribute('data-path');
        // Check if filePath is an absolute URL
        const isAbsoluteURL = filePath.startsWith('http://') || filePath.startsWith('https://');
        const link = document.createElement('a');
        // Set href based on whether filePath is an absolute URL
        link.href = isAbsoluteURL ? filePath : './' + filePath;
        link.download = filePath.substring(filePath.lastIndexOf('/') + 1);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    });
});

</script>