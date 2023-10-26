import axios from 'axios';

async function run(text) {
    try {
        const response = await axios.post(
            'https://api.sapling.ai/api/v1/aidetect',
            {
                key: 'OGE1TGHIQLUHAABHHHZ84NVZ5RUIMGPQ',
                text,
            },
        );
        const {status, data} = response;
        console.log({status});
        console.log(JSON.stringify(data, null, 4));
    } catch (err) {
        const { msg } = err.response.data;
        console.log({err: msg});
    }
}

run('This is sample text').then(data => {
    document.getElementById('result').innerText = JSON.stringify(data); 
  })