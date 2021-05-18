<script lang="typescript">
    import { channel } from "./scripts/xana";
    import {host, getData} from "./scripts/utils";
    export let callId: string;

    const startCallOr404 = async() => {
        const res = await getData(host + "call/" + callId);
        return res.json();
    }

    let videoText = "";
    let getVideo = async () => {
        let constraints = { audio: false, video: true };
        try{
            let video = document.querySelector("video");
            videoText = "Getting video...";
            let stream = await navigator.mediaDevices.getUserMedia(constraints);
            video.srcObject = stream;
            video.play();
            videoText = "Playing video";
            channel.send(JSON.stringify({ message: "Hello" }));
        }
        catch(err){
            console.log(err);
        }
    };
</script>

{#await startCallOr404()}
    <main>
        <p>Starting call...</p>
    </main>
{:then callData}
    <main>
        <h3> Chamada: {JSON.parse(callData).callId} </h3>
        <video kind="captions" src=""></video>
        <button on:click={getVideo}>Get video</button>
        <p>{videoText}</p>
    </main>
{:catch err}
    <main>
        <h1>A chamada desejada não existe!</h1>
    </main>
{/await}

<style>
    main{
        display: flex;
        width: 100%;
        height: 100%;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    video{
        width: 50%
    }

    button{
        padding: 1rem;
    }
</style>
