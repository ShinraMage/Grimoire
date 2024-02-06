# Tools

Here are the converter of md file to html files.
The format is from


## ★ Game Proposal Converter
This is game proposal template, from https://stm4h4.com/downloads/
<div class="download-template">proposal/proposal.md</div>

<br><br>

## ★ Outline Converter
This is story outline template, from https://stm4h4.com/downloads/
<div class="download-template">outline/outline.md</div>

<br><br>

## ★ Character Card, Basic ver Converter
this is char card template from https://stm4h4.com/downloads/
<div class="download-template">character/basic.md</div>

<br><br>

## ★ Character Card, Advance ver Converter
this is char card template from https://stm4h4.com/downloads/
<div class="download-template">character/advance.md</div>




<script>
    function DownloadTemplate(filePath, fileName, parentDiv) {
        // Create a button element
        var button = document.createElement('button');
        button.textContent = 'Download template of ' + fileName;

        // Add a click event listener to trigger the download
        button.addEventListener('click', function() {
            // Convert the fileName to lowercase
            var lowerCaseFileName = fileName.toLowerCase();

            // Create a new anchor element dynamically with the provided file path
            var element = document.createElement('a');
            element.setAttribute('href', filePath);

            // Set the download attribute with the desired lowercase file name including the .md extension
            element.setAttribute('download', lowerCaseFileName + '.md');

            // Insert the button immediately after the corresponding div
            parentDiv.insertAdjacentElement('afterend', element);
            
            // Force click and remove it
            element.click();
            document.body.removeChild(element);
        });

        // Insert the button immediately after the corresponding div
        parentDiv.insertAdjacentElement('afterend', button);
    }

    // Find all elements with the class "download-template" and create download buttons for them
    var templateElements = document.querySelectorAll('.download-template');
    templateElements.forEach(function(element) {
        var filePath = element.textContent; // Get the file path from the element's text content
        var fileName = filePath.replace('.md', ''); // Extract the filename without extension
        DownloadTemplate(filePath, fileName, element);
    });
</script>