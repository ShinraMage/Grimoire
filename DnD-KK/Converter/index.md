---
layout: page/note/basic
---

# KK魔法學院 課程轉換器

<script src="https://cdn.jsdelivr.net/npm/markdown-it@14/dist/markdown-it.min.js"></script>
<style>
  button, input[type=file] { margin-right: 0.5em; margin-bottom: 1em; }
  #output { border: 1px solid #ccc; padding: 1em; min-height: 600px; margin-top: 1em; }
</style>

<div>
  <button data-template="slides.html">Slides</button>
  <button data-template="mindmap.html">Mindmap</button>
</div>

<input type="file" id="fileInput" accept=".md" disabled>
<button id="downloadBtn" disabled>Download HTML</button>

<iframe id="output" style="width: 100%; height: 600px;"></iframe>

<script>
    const md = window.markdownit({ html: true });
    let templateHTML = '';
    let selectedTemplate = '';
    let generatedHTML = '';
    
    async function loadTemplate(name) {
      const res = await fetch(name);
      if (!res.ok) {
        alert(`Failed to load template: ${name}`);
        return;
      }
      templateHTML = await res.text();
      selectedTemplate = name;
      document.getElementById('fileInput').disabled = false;
      
      const iframe = document.getElementById('output');
      const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
      iframeDoc.open();
      iframeDoc.write(`<p style="padding: 1em; color: #666;">Template <b>${name}</b> loaded. Now upload a Markdown file.</p>`);
      iframeDoc.close();
    }
    
    async function convertAndInsert(file) {
      const text = await file.text();
      const html = md.render(text);
      if (!templateHTML) {
        alert('Please choose a template first.');
        return;
      }
      
      // Use regex to match any whitespace variation of the placeholder
      generatedHTML = templateHTML.replace(/\{\{\s*Target\s*\}\}/gi, html);
      
      // Write content to iframe
      const iframe = document.getElementById('output');
      const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
      iframeDoc.open();
      iframeDoc.write(generatedHTML);
      iframeDoc.close();
      
      document.getElementById('downloadBtn').disabled = false;
    }
    
    function downloadFile() {
      if (!generatedHTML) return;
      const blob = new Blob([generatedHTML], { type: 'text/html' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = selectedTemplate.replace('.html', '-output.html');
      a.click();
      URL.revokeObjectURL(url);
    }
    
    document.querySelectorAll('button[data-template]').forEach(btn => {
      btn.addEventListener('click', () => loadTemplate(btn.dataset.template));
    });
    
    document.getElementById('fileInput').addEventListener('change', e => {
      const file = e.target.files[0];
      if (file) convertAndInsert(file);
    });
    
    document.getElementById('downloadBtn').addEventListener('click', downloadFile);
</script>