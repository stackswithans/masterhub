<script lang="typescript">
    import {reverse, postData} from "../scripts/utils";
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

    p{
        color: white;
        border: None;
    }

    div{
        margin-top: 1rem;
        display: flex;
    }

    .parent :global(.spacing){
        margin-right: 1rem;
    }
</style>
