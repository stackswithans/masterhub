<script lang="typescript">
    import { host, postData, getData } from "./scripts/utils";
    import { navigate } from "svelte-routing";

    let newCallId = "";
    let callId = ""; 
    const createNewCall = async () =>{
        try{
            const res = await postData(host + "call/", { user: "" });
            newCallId = JSON.parse(res).callId;
        }
        catch(err){
            console.log(err);
        }
    };

    const joinCall = async () =>{
        navigate(`call/${callId}`);
    };
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
