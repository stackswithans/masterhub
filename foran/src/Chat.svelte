<script lang="typescript">
    import { host } from "./config";
    let newCallId = "";
    let callId = ""; 

    const createNewCall = async () =>{
        try{
            const res =  await fetch(host + "/call/", {
                method: 'POST',
                mode: 'cors',
                credentials: 'same-origin',
                headers: {
                  'Content-Type': 'application/json'
                },
                redirect: 'follow', 
                referrerPolicy: 'no-referrer',
                body: JSON.stringify({ user: "" })
            });

            res.json().then( data => {
                

                newCallId = JSON.parse(data).callId;
            });
        }
        catch(err){
            console.log(err);
        }
    };

    const joinCall = () =>{};
</script>

<main>
    <button on:click={createNewCall} >Create new call</button>
    <p>{newCallId}</p>
    <h2>or</h2>
    <p>Join an existing call:</p>
    <input bind:value={callId} type="text" placeholder="Call code here" id="join-input"/>
    <button on:click={joinCall}>Join</button>
</main>

<style>
    main{
        display: flex;
        width: 100%;
        height: 100%;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    button{
        padding: 1rem;
    }
</style>
