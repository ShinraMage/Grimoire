# Converter 

```
upload yml file as content and replace {{}} in html
```

## Online Converter

<button class="upload-template" data-target-iframe="OutPreview">Upload template.html</button>
<button class="upload-yml" data-target-iframe="OutPreview">Upload .yml</button>
<button class="download-result" data-for="OutPreview">outcome.html</button>
<button class="a4-print" data-for="OutPreview">Print PDF</button>
<iframe id="OutPreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

<script>
let templateHtmlContent = '';

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
            console.log("Template HTML content loaded:", templateHtmlContent);
            displayInIframe(templateHtmlContent, targetIframeID); // Display uploaded template in iframe
        };
        
        reader.readAsText(file);
    };

    fileInput.click();
});

document.querySelector('.upload-yml').addEventListener('click', function() {
    const targetIframeID = this.getAttribute('data-target-iframe');
    if (!templateHtmlContent) {
        alert("Please upload a template.html first.");
        return;
    }
    
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = '.yml';
    
    fileInput.onchange = e => {
        const file = e.target.files[0];
        if (!file) return;
        
        const reader = new FileReader();
        reader.onload = function(e) {
            let ymlContent = e.target.result;
            console.log("Original YAML content:", ymlContent);

            // Custom parsing logic
            const parsedContent = parseYamlContent(ymlContent);
            console.log("Parsed custom YAML content:", parsedContent);

            const convertedHtml = convertYamlContentToHtml(parsedContent, templateHtmlContent);
            console.log("Converted HTML content:", convertedHtml);
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

document.querySelector('.a4-print').addEventListener('click', function() {
    const iframeId = this.getAttribute('data-for');
    const iframe = document.getElementById(iframeId);
    injectPrintStyles(iframe);
    iframe.focus();
    iframe.contentWindow.print();
});

function parseYamlContent(ymlContent) {
    const lines = ymlContent.split('\n');
    const result = {};
    let currentKey = null;
    let currentValue = [];

    lines.forEach(line => {
        if (line.trim() === '') {
            return;
        }

        const [key, ...value] = line.split(':');
        if (value.length > 0) {
            if (currentKey) {
                result[currentKey] = currentValue.join('<br>');
            }
            currentKey = key.trim();
            currentValue = [value.join(':').trim()];
        } else {
            currentValue.push(line.trim());
        }
    });

    if (currentKey) {
        result[currentKey] = currentValue.join('<br>');
    }

    return result;
}

function convertYamlContentToHtml(parsedContent, templateHtml) {
    // Load the template HTML
    let htmlOutput = templateHtml;

    // Replace placeholders in the template with actual content from the parsed YAML content
    Object.entries(parsedContent).forEach(([key, value]) => {
        // Remove first and last double quotes if present
        value = value.substring(1, value.length - 1);
        if (value.startsWith('br>')) {
            value = value.substring(4);
        }

        // Create a regex to find the placeholder in the HTML template
        const regex = new RegExp(`\\{\\{${key}\\}\\}`, 'g');
        // Replace the placeholder with the actual content
        htmlOutput = htmlOutput.replace(regex, value);
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

function injectPrintStyles(iframe) {
    const printStyle = `
        <style>
            * {
                color: black !important;
                background: white !important;
            }
        </style>
    `;
    const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
    const head = iframeDoc.getElementsByTagName('head')[0];
    head.insertAdjacentHTML('beforeend', printStyle);
}
</script>






## examples
#### Save the Cat Beatsheet
* [beetsheat.html](https://raw.githubusercontent.com/aimageguild/GPTs/main/Design/Navi%20-%20Beat%20Sheet%20Writer/Beat%20Sheet.html)
* [beetsheat.yml](https://raw.githubusercontent.com/aimageguild/GPTs/main/Design/Navi%20-%20Beat%20Sheet%20Writer/Beat%20Sheet.yml)
* You can use [GPTs - Navi](https://chat.openai.com/g/g-NsZTxNrJJ) to gen this beatsheet.yml

#### tables from [摩訶聖 StM4H4](https://stm4h4.com/downloads/)
* Proposal
  * [proposal.yml template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/proposal/proposal.yml)
  * [proposal.html template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/proposal/proposal.html)
  * You can use [GPTs - Vixen](https://chat.openai.com/g/g-oR0tADta6) to gen proposal.yml 
* Outline
  * [Outline.yml template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/outline/outline.yml)
  * [Outline.html template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/outline/outline.html)
* Character Card
  * [Character.yml template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/character/character.yml)
  * [Char_Basic.html template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/character/basic.html)
  * [Char_Advance.html template](https://raw.githubusercontent.com/posetmage/GameDesign/master/Tool/character/advance.html)
  * You can use [GPTs - Scarlett](https://chat.openai.com/g/g-LD06QK4Bt) to gen Character.yml 

