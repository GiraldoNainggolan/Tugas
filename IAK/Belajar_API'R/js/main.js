// Ini adalah versi pertama langsung dari Rapid-Apinya
// const url = 'https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions';
// const options = {
// 	method: 'POST',
// 	headers: {
// 		'x-rapidapi-key': '9173484eeamshca65f65e83c008ap137197jsnc76d37759a45',
// 		'x-rapidapi-host': 'cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com',
// 		'Content-Type': 'application/json'
// 	},
// 	body: {
// 		messages: [
// 			{
// 				role: 'user',
// 				content: 'Hello, how is it going?'
// 			}
// 		],
// 		model: 'gpt-4o',
// 		max_tokens: 100,
// 		temperature: 0.9
// 	}
    
// };

// try {
// 	const response = await fetch(url, options);
// 	const result = await response.text();
// 	console.log(result);
// } catch (error) {
// 	console.error(error);
// }

// Ini adalah versi kedua yang aku perbaiki
// const url = 'https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions';
// const options = {
// 	method: 'POST',
// 	headers: {
// 		'x-rapidapi-key': '9173484eeamshca65f65e83c008ap137197jsnc76d37759a45',
// 		'x-rapidapi-host': 'cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com',
// 		'Content-Type': 'application/json'
// 	},
// 	body: JSON.stringify({
// 		messages: [
// 			{
// 				role: 'user',
// 				content: 'Hello, how is it going?'
// 			}
// 		],
// 		model: 'gpt-4o',
// 		max_tokens: 100,
// 		temperature: 0.9
// 	})
// };

// try {
// 	const response = await fetch(url, options);
// 	const result = await response.text();
// 	console.log(result);
// } catch (error) {
// 	console.error(error);
// }

// Ini adalah versi ketiga yang aku perbaiki dengan ai
// const url = 'https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions';
// const options = {
// 	method: 'POST',
// 	headers: {
// 		'x-rapidapi-key': '9173484eeamshca65f65e83c008ap137197jsnc76d37759a45',
// 		'x-rapidapi-host': 'cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com',
// 		'Content-Type': 'application/json'
// 	},
// 	body: JSON.stringify({
// 		messages: [
// 			{
// 				role: 'user',
// 				content: 'Hello, how is it going?'
// 			}
// 		],
// 		model: 'gpt-4o',
// 		max_tokens: 100,
// 		temperature: 0.9
// 	})
// };

// try {
// 	const response = await fetch(url, options);
// 	const result = await response.text();
// 	console.log(result);
// } catch (error) {
// 	console.error(error);
// }


const url = 'https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions';
const options = {
    method: 'POST',
    headers: {
        'x-rapidapi-key': '9173484eeamshca65f65e83c008ap137197jsnc76d37759a45',
        'x-rapidapi-host': 'cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com',
        'Content-Type': 'application/json'
    }
};

document.getElementById("sendBtn").addEventListener("click", async () => {
    const userMessage = document.getElementById("userMessage").value;

    // Set up body content for API request
    const bodyContent = JSON.stringify({
        messages: [
            {
                role: 'user',
                content: userMessage
            }
        ],
        model: 'gpt-4o',
        max_tokens: 100,
        temperature: 0.9
    });

    try {
        const response = await fetch(url, {
            ...options,
            body: bodyContent
        });
        
        if (!response.ok) {
            throw new Error(`Error ${response.status}: ${response.statusText}`);
        }

        const result = await response.json();
        document.getElementById("responseOutput").textContent = result.choices[0].message.content;
    } catch (error) {
        document.getElementById("responseOutput").textContent = `Error: ${error.message}`;
    }
});
