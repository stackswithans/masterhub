<script lang="typescript">
    import { channel } from "./xana";
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

<main>
    <video kind="captions" src=""></video>
    <button on:click={getVideo}>Get video</button>
    <p>{videoText}</p>
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

    video{
        width: 50%
    }

    button{
        padding: 1rem;
    }
</style>
