<script lang="typescript">
    import {reverse, postData} from "./scripts/utils";
    import {navigate} from "svelte-routing";

    let callId = ""; 
    const createNewCall = async () => {
        try{
            const res = await postData(reverse("call"), { user: "Sténio Jacinto" });
            callId = JSON.parse(res).callId;
        }
        catch(err){
            console.log(err);
        }
    };

    const joinCall = () =>{
        navigate(`call/${callId}`, {replace: true});
    };
</script>

<main>
    <p>Join an existing call or create a new one:</p>
    <input bind:value={callId} type="text"  id="join-input"/>
    <div>
        <button on:click={joinCall}>Join</button>
        <button on:click={createNewCall} >New call</button>
    </div>
</main>

<style>
    main{
        display: flex; width: 100%;
        height: 100%;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: #36413E;
    }

    p, input{
        color: white;
        border: None;
    }

    input{
        background: transparent;
        border-bottom: 3px solid #4A5955;
    }

    input:focus{
        outline: None;
    }

    div{
        margin-top: 1rem;
    }

    div button:first-child{
        margin-right: 1rem;

    }

    button{
        padding: 0.5rem;
        color: white;
        border: None;
        background-color: #4A5955;
    }

    button:hover{
        cursor: pointer;
    }
</style>
