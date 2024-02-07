---
layout: notes
---

# Tools

Here are the converter of md file to html files.
The format is from


## ★ Game Proposal Converter
<button class="download-template" data-path="proposal/proposal.md">Download proposal.md template</button>
<button class="md2html-converter" data-target-iframe="gameProposalPreview">proposal/proposal.html.txt</button>
<iframe id="gameProposalPreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

## ★ Outline Converter
<button class="download-template" data-path="outline/outline.md">Download outline.md template</button>
<button class="md2html-converter" data-target-iframe="gameOutlinePreview">outline/outline.html.txt</button>
<iframe id="gameOutlinePreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

## ★ Character Card, Basic ver Converter
<button class="download-template" data-path="character/basic.md">Download Char_Basic.md template</button>
<button class="md2html-converter" data-target-iframe="CharBasicPreview">character/basic.html.txt</button>
<iframe id="CharBasicPreview" width="100%" height="600px" style="background-color: white;"></iframe>
<br><br>

## ★ Character Card, Advance ver Converter
<button class="download-template" data-path="character/advance.md">Download Char_Advance.md template</button>
<button class="md2html-converter" data-target-iframe="CharAdvPreview">character/advance.html.txt</button>
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
                // Derive the HTML file path from the button's content
                var htmlFilePath = this.textContent;
                
                // Find the target iframe ID from the button's data attribute
                var targetIframeID = this.getAttribute('data-target-iframe');
                
                // Find the target iframe by ID
                var targetIframe = document.getElementById(targetIframeID);
                
                // Update the 'src' attribute of the iframe with the derived path
                targetIframe.src = htmlFilePath;
            });
        });
    });
</script>
