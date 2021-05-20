<script lang="typescript">
    import Input from "./Input.svelte";
    import { joinCall } from "./scripts/xana";
    import {reverse, getData} from "./scripts/utils";

    export let callId: string;
    let user = "";
    let videoText = "";

    const startCallOr404 = async() => {
        const res = await getData(reverse("call", [callId]));
        if(res.status == 404){
            throw Error("Bad call id");
        }
        return res.json();
    }
    
    let getVideo = async () => {
        let constraints = { audio: false, video: true };
        try{
            //TODO: Fix this race condition: video can be null cause tag may not
            //Have been rendered by the time getVideo is called
            let stream = null;
            if(!navigator.mediaDevices)
                throw new Error("mediaDevices not supported in this browser");
            stream = await navigator.mediaDevices.getUserMedia(constraints);
            if (stream == null){
                videoText = "Impossível encontrar uma câmera"; 
                throw new Error("Impossível encontrar uma camera");
            }
            let remoteVideo = document.querySelector("#remote-video") as HTMLMediaElement;
            let localVideo = document.querySelector("#local-video") as HTMLMediaElement;
            videoText = "Getting video...";
            localVideo.srcObject = stream;
            localVideo.play();
            videoText = "Playing video";
            //Join the video call
            joinCall(callId, stream, (track: MediaStreamTrack, streams: readonly MediaStream[]) => {
                track.onunmute = () =>{
                    console.log("Video available");
                    if(remoteVideo.srcObject) return;
                    remoteVideo.srcObject = streams[0];
                    remoteVideo.play();
                }
            });
        }
        catch(err){
            console.log(err);
        }
    };

    const promise = startCallOr404();
    promise.then(data => {
        getVideo();
    });

</script>

<main>
{#if user === ""}
    <div id="name-prompt">
        <p>Por favor introduza o seu nome</p>
        <Input bind:value={user}/>
    </div>
{:else}
    <aside>
        <div id="call-info">
            <h3>Outro Boy</h3>
        </div>
        <video id="remote-video" kind="captions" src=""></video>
        <p>{videoText}</p>
    </aside>
    <aside>
        <video id="local-video" kind="captions" src=""></video>
    </aside>
    <h1>A chamada desejada não existe!</h1>
{/if}
</main>

<style>
    #name-prompt{
        display: flex;
        box-sizing: border-box;
        flex-direction: column;
        text-align: center;
        color: white;
    }

    main{
        display: flex;
        width: 100%;
        height: 100%;
        box-sizing: border-box;
        justify-content: center;
        align-items: center;
        background-color: var(--p-color);
    }

    aside{
        display: flex;
        flex-direction: column;
        justify-content: first;
        align-items: center;
        box-sizing: border-box;
    }

    aside:first-child{
        width: 80%;
    }

    aside:nth-child(2){
        width: 20%;
    }

    video{
        position: relative;
        width: 80%; 
    }
</style>
