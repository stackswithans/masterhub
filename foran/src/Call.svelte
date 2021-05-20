<script lang="typescript">
    import Input from "./Input.svelte";
    import Button from "./Button.svelte";
    import CallBox from "./CallBox.svelte";
    import { onMount, tick } from "svelte";
    import { joinCall } from "./scripts/xana";
    import {reverse, getData} from "./scripts/utils";

    export let callId: string;
    let user = "";

    let loading = true; 
    let callFound = null;
    let enterCall = false;

    let remoteVideo: HTMLVideoElement; 
    let localVideo: HTMLVideoElement; 

    let getVideo = async () => {
        let constraints = { audio: false, video: true };
        try{
            if(!navigator.mediaDevices)
                throw new Error("mediaDevices not supported in this browser");
            let stream = await navigator.mediaDevices.getUserMedia(constraints);
            if (stream == null){
                throw new Error("Impossível encontrar uma camera");
            }
            //remoteVideo = document.querySelector("#remote-video") as HTMLMediaElement;
            //localVideo = document.querySelector("#local-video") as HTMLMediaElement;
            localVideo.srcObject = stream;
            localVideo.play();
            //Join the video call
            joinCall(callId, stream, (track: MediaStreamTrack, streams: readonly MediaStream[]) => {
                track.onunmute = () => {
                    if(remoteVideo) return;
                    remoteVideo.srcObject = streams[0];
                    remoteVideo.play()
                }
            });
        }
        catch(err){
            console.log(err);
        }
    };

    const doCall = async () => {
        enterCall = true;
        await tick();
        getVideo();
    }

    onMount(async() => {
        const res = await getData(reverse("call", [callId]));
        loading = false;
        if(res.status == 404){
            return;
        }
        callFound = true;
    });

</script>

<main>
{#if loading}
    <p>Carregando dados a cerca da chamada...</p>
{:else if !loading && callFound}
    {#if !enterCall}
        <div id="name-prompt">
            <p>Por favor introduza o seu nome para entrar na chamada</p>
            <Input bind:value={user}/>
            <Button on:click={doCall} text="Join"/>
        </div>
    {:else}
        <div class="callboxes">
            <CallBox caption={user} bind:video={localVideo}/>
        </div>
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

    .callboxes{
        display:flex;
        box-sizing: border-box;
        justify-content: space-evenly;
        align-items: center;
        width: 100%;
        height: 100%;
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
</style>
