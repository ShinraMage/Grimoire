# Converter 

```
upload yml file as content and replace {{ }} in html
```
## Online Converter

<button class="upload-template" data-target-iframe="OutPreview">Upload template.html</button>
<button class="upload-yml" data-target-iframe="OutPreview">Upload .yml</button>
<button class="download-result" data-for="OutPreview">Download Result</button>
<button class="a4-print" data-for="OutPreview">Print PDF</button>
<iframe id="OutPreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

<script src="https://cdn.jsdelivr.net/npm/js-yaml@4/dist/js-yaml.min.js"></script>
<script src="https://posetmage.com/cdn/js/parser/convertYamlToHtml.js"></script>

<script>
    let templateHtmlContent = '';

    function uploadAndReadFile(acceptType, callback) {
        const fileInput = document.createElement('input');
        fileInput.type = 'file';
        fileInput.accept = acceptType;

        fileInput.onchange = e => {
            const file = e.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = function(e) {
                callback(e.target.result);
            };
            reader.readAsText(file);
        };
        fileInput.click();
    }

    document.querySelector('.upload-template').addEventListener('click', function() {
        const targetIframeID = this.getAttribute('data-target-iframe');
        uploadAndReadFile('.html', (htmlContent) => {
            templateHtmlContent = htmlContent;
            displayInIframe(templateHtmlContent, targetIframeID); // Display uploaded template in iframe
        });
    });

    document.querySelector('.upload-yml').addEventListener('click', function() {
        const targetIframeID = this.getAttribute('data-target-iframe');
        if (!templateHtmlContent) {
            alert("Please upload a template.html first.");
            return;
        }

        uploadAndReadFile('.yml', (ymlContent) => {
            let convertedHtml;
            try {
                // Use the imported convertYamlToHtml function
                convertedHtml = convertYamlToHtml(ymlContent, templateHtmlContent);
                displayInIframe(convertedHtml, targetIframeID); // Update iframe with merged content
            } catch (error) {
                console.error("Conversion Error:", error);
                alert(`Error converting YAML to HTML: ${error.message}`);
            }
        });
    });

    document.querySelector('.download-result').addEventListener('click', function() {
        const iframeId = this.getAttribute('data-for');
        const iframeContent = document.getElementById(iframeId).contentDocument.documentElement.outerHTML;
        const blob = new Blob([iframeContent], {type: 'text/html'});
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'converted.html';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    });

    function displayInIframe(htmlContent, iframeId) {
        const targetIframe = document.getElementById(iframeId);
        const blob = new Blob([htmlContent], {type: 'text/html'});
        const url = URL.createObjectURL(blob);
        targetIframe.src = url;
    }

    document.querySelector('.a4-print').addEventListener('click', function() {
        const iframeId = this.getAttribute('data-for');
        const iframe = document.getElementById(iframeId);
        iframe.focus();
        iframe.contentWindow.print();
    });

</script>

## examples
#### Save the Cat Beatsheet
* [beatsheet.html](https://raw.githubusercontent.com/aimageguild/GPTs/main/Design/Navi%20-%20Beat%20Sheet%20Writer/Beat%20Sheet.html)
* [beatsheet.yml](https://raw.githubusercontent.com/aimageguild/GPTs/main/Design/Navi%20-%20Beat%20Sheet%20Writer/Beat%20Sheet.yml)

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