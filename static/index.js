// Let's write two version of this, just for fun.
window.onload = function() {
    let status = document.getElementById('status');
    let input = document.querySelector('input[name="csv"]');

    input.addEventListener('change', function(evt) {
        let file = this.files[0];
        console.log(this.files[0]);
        UploadFile(file, status);
    });
    
}


function UploadFile(file, status) {
    let reader = new FileReader();
    let xhr = new XMLHttpRequest();

    xhr.open("POST", "/process/");
    xhr.overrideMimeType("text/plain; charset=x-user-defined-binary");

    reader.onload = function(evt) {
        status.innerHTML = "File sent, awaiting response...";
        xhr.send(evt.target.result);
    }
    
    xhr.onload = function(evt) {
        let response = JSON.parse(evt.target.response);

        if (response.hasOwnProperty('error')) {
            status.innerHTML = response['error'];
        }
        else {
            status.innerHTML = 'CSV Parsing successful';
            let output = document.getElementById('output');

            console.log(output);
            console.log("hello");
            let lines = response['data'].split('\n');

            for (var i = 0; i < lines.length; i++) {
                let new_line = document.createElement('div');
                new_line.className = "output-row"
                new_line.innerHTML = lines[i];
                output.appendChild(new_line);
            }

        }
    }
    
    
    reader.readAsBinaryString(file);
}