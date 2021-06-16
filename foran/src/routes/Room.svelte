<script lang="typescript">
    import HomeLayout from "../components/HomeLayout.svelte";
    import { onMount } from "svelte";

    let remoteVideo: HTMLVideoElement; 
    let localVideo: HTMLVideoElement; 

    let getVideo = async () => {
        let constraints = { audio: false, video: true };
        let stream = null;
        try{
            if(navigator.mediaDevices === undefined) throw new Error("Browser does not support mediaDevices");
            stream = await navigator.mediaDevices.getUserMedia(constraints);
            if (stream == null){
                throw new Error("Impossível encontrar uma câmera");
            }
            remoteVideo.srcObject = stream;
            localVideo.srcObject = stream;
            remoteVideo.play();
            localVideo.play();
        }
        catch(err){
            console.log(err);
        }
    };
    onMount(() => { getVideo() });
</script>

<HomeLayout>
    <div class="main-sector">
        <div class="master-camera">
            <video bind:this={remoteVideo} id="remote-video" src=""></video>
        </div>
        <div class="video-wrapper">
            <video bind:this={localVideo} width="100%" class="student-camera"></video>
        </div>
        <div class="classroom-options">
            <i class="fas fa-microphone fa-lg"></i>
            <i class="fas fa-volume-up fa-lg"></i>
            <i class="fas fa-phone-alt fa-lg"></i>
        </div>
    </div>
</HomeLayout>

<style>
    .main-sector{
        padding: 2em;
        width: 100%;
        height: 93vh;
        display: flex;
        gap: 2rem;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    .video-wrapper{
        max-width: 20%;
        max-height: 20%;
    }

    .student-camera{
        width: 100%;
        height: 100%;
    }


    .master-camera{
        position: flex;
        border-radius: 4px;
        max-height: 50%;
        max-width: 50%;
    }

    #remote-video{
        max-width: 100%;
        max-height: 100%;
    }

    .classroom-options{
        z-index: 2;
        position: relative;
        display: flex;
        gap: 2em;
        font-size: 0.8em;
        padding: 0 2em;
    }

    .fa-microphone, .fa-volume-up{
        background-color: white;
        border-radius: 100px;
        padding: 0.5em;
    }

    .fa-phone-alt{
        background-color: red;
        border-radius: 100px;
        padding: 0.5em;
        color: rgb(163, 163, 163);
    }

</style>
