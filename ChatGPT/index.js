function submitForm(e) {
    e.preventDefault();
    getData();
}

async function getData() {
    let userData = document.get.getElementById("input").value.trim();
    if(userData === "") return false;

    document.getElementById("messages").innerHTML = `<div class="mess-user">
        <p>${userData}</p>
    </div>` + document.getElementById("messages").innerHTML
    document.get.getElementById("input").value = ""

    const API = "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";

    try {
        const response =  await fetch('https://api.openai.com/v1/chat/completions'),{
            method: 'POST',
            headers: {'Authorization': `Bearer ${API}`,'Content-Type': 'application/json'},
            body: JSON.stringify({
                model: 'gpt-3.5-turbo',
                messages: [{role: 'user', content: userData},
                max_tokens = 100
            })
        }
        const data = await response.json()

        document.getElementById("messages").innerHTML = `<div class="mess-chat">
            <p>${data.choices[0].message.content}</p>
        </div>` + document.getElementById("messages").innerHTML

    } catch(error) {
        console.error('Error: ', error)
    }
}