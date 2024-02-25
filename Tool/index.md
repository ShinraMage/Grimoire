---
layout: page/note/basic
---

# Tools

## Converter 

```
upload yml file as content and replace {{}} in html
```


<button class="upload-template" data-target-iframe="OutPreview">Upload template.html</button>
<button class="upload-yml" data-target-iframe="OutPreview">Upload .yml</button>
<button class="download-result" data-for="OutPreview">outcome.html</button>
<iframe id="OutPreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

<script src="https://cdn.jsdelivr.net/npm/js-yaml@4/dist/js-yaml.min.js"></script>

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
            const ymlContent = e.target.result;
            const convertedHtml = convertYamlContentToHtml(ymlContent, templateHtmlContent);
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

function convertYamlContentToHtml(yamlContent, templateHtml) {
    // Parse the YAML content into a JavaScript object
    const parsedContent = jsyaml.load(yamlContent);

    // Load the template HTML
    let htmlOutput = templateHtml;

    // Replace placeholders in the template with actual content from the YAML file
    Object.entries(parsedContent).forEach(([key, value]) => {
        // For simplicity, we assume value is directly a string or can be represented as one
        // Create a regex to find the placeholder in the HTML template
        const regex = new RegExp(`\\{\\{${key}\\}\\}`, 'g');
        // Replace the placeholder with the actual content
        htmlOutput = htmlOutput.replace(regex, value.toString());
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
