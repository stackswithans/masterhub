<script lang="typescript">
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
        }
        catch(err){
            console.log(err);
        }
    };
</script>

<main>
    <video kind="captions" src=""></video>
    <p>{videoText}</p>
    <button on:click={getVideo}>Get video</button>
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
