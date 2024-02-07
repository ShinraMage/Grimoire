---
layout: notes
---

# Tools

## ★ Game Proposal Converter
<button class="download-template" data-path="proposal/proposal.md">Download proposal.md template</button>
<button class="md2html-converter" data-target-iframe="gameProposalPreview" data-path="proposal/proposal.html.txt">Preview proposal</button>
<iframe id="gameProposalPreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>


## ★ Outline Converter
<button class="download-template" data-path="outline/outline.md">Download outline.md template</button>
<button class="md2html-converter" data-target-iframe="gameOutlinePreview" data-path="outline/outline.html.txt">Preview Outline</button>
<iframe id="gameOutlinePreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

## ★ Character Card, Basic ver Converter
<button class="download-template" data-path="character/basic.md">Download Char_Basic.md template</button>
<button class="md2html-converter" data-target-iframe="CharBasicPreview" data-path="character/basic.html.txt">Preview Char_Basic</button>
<iframe id="CharBasicPreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

## ★ Character Card, Advance ver Converter
<button class="download-template" data-path="character/advance.md">Download Char_Advance.md template</button>
<button class="md2html-converter" data-target-iframe="CharAdvPreview" data-path="character/advance.html.txt">Preview Char_Advance</button>
<iframe id="CharAdvPreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>


<script>
    document.querySelectorAll('.download-template').forEach(button => {
        button.addEventListener('click', function() {
            // Retrieve the file path from the button's data-path attribute
            var filePath = this.getAttribute('data-path');
            // Create a new <a> element
            var link = document.createElement('a');
            // Set the href to the file path, assuming files are in a publicly accessible directory
            link.href = './' + filePath;
            // Use the download attribute to specify the filename; this can be tailored as needed
            link.download = filePath.substring(filePath.lastIndexOf('/') + 1);
            // Append the <a> element to the body (temporarily) to make it clickable
            document.body.appendChild(link);
            // Programmatically click the <a> element to trigger the download
            link.click();
            // Remove the <a> element from the body
            document.body.removeChild(link);
        });
    });
</script>

<script type="text/javascript">
    document.addEventListener('DOMContentLoaded', function() {
        // Select all converter buttons
        var converterButtons = document.querySelectorAll('.md2html-converter');
        
        // Add click event listener to each button
        converterButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                // Retrieve the HTML file path from the button's data-path attribute
                var htmlFilePath = this.getAttribute('data-path');
                
                // Use fetch API to get the content of the .txt file
                fetch('./' + htmlFilePath) // Adjust the path as necessary
                    .then(response => response.text())
                    .then(data => {
                        // Create a blob of type 'text/html' with the content
                        var blob = new Blob([data], { type: 'text/html' });
                        
                        // Create a URL for the blob
                        var url = URL.createObjectURL(blob);
                        
                        // Find the target iframe ID from the button's data-target-iframe attribute
                        var targetIframeID = this.getAttribute('data-target-iframe');
                        
                        // Find the target iframe by ID
                        var targetIframe = document.getElementById(targetIframeID);
                        
                        // Update the 'src' attribute of the iframe with the blob URL
                        targetIframe.src = url;
                    })
                    .catch(error => console.error('Error loading the file:', error));
            });
        });
    });
</script>
