<script lang="typescript">
    import Input from "./Input.svelte";
    import Button from "./Button.svelte";
    import { onMount, tick } from "svelte";
    import { joinCall } from "./scripts/xana";
    import {reverse, getData} from "./scripts/utils";

    export let callId: string;
    let user = "";

    let loading = true; 
    let callFound = null;

    let remoteVideo: HTMLMediaElement; 
    let localVideo: HTMLMediaElement; 

    let getVideo = async () => {
        let constraints = { audio: false, video: true };
        try{
            if(!navigator.mediaDevices)
                throw new Error("mediaDevices not supported in this browser");
            let stream = await navigator.mediaDevices.getUserMedia(constraints);
            if (stream == null){
                throw new Error("Impossível encontrar uma camera");
            }
            localVideo.srcObject = stream;
            localVideo.play();
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

    onMount(async() => {
        const res = await getData(reverse("call", [callId]));
        loading = false;
        if(res.status == 404){
            return;
        }
        callFound = true;
        //Wait for changes to the DOM
        await tick();
        remoteVideo = document.querySelector("#remote-video") as HTMLMediaElement;
        localVideo = document.querySelector("#local-video") as HTMLMediaElement;
        getVideo();
    });

</script>

<main>
{#if loading}
    <p>Carregando dados a cerca da chamada...</p>
{:else if !loading && callFound}
    {#if user === ""}
        <div id="name-prompt">
            <p>Por favor introduza o seu nome para entrar na chamada</p>
            <Input bind:value={user}/>
            <Button text="Join"/>
        </div>
    {:else}
        <aside>
            <video id="remote-video" kind="captions" src=""></video>
        </aside>
        <aside>
            <video id="local-video" kind="captions" src=""></video>
        </aside>
        <h1>A chamada desejada não existe!</h1>
    {/if}
{:else}
    <p>A chamada não foi encontrada.</p>
{/if}
</main>

<style>
    #name-prompt{
        display: flex;
        box-sizing: border-box;
        flex-direction: column;
        text-align: center;
        justify-content: center;
        align-items: center;
    }

    main{
        display: flex;
        width: 100%;
        height: 100%;
        box-sizing: border-box;
        justify-content: center;
        align-items: center;
        background-color: var(--p-color);
        color: white;
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
