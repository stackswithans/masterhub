<script lang="typescript">
    import { joinCall } from "./scripts/xana";
    import {host, getData} from "./scripts/utils";

    export let callId: string;
    let videoText = "";

    const startCallOr404 = async() => {
        const res = await getData(host + "call/" + callId);
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
            let stream = await navigator.mediaDevices.getUserMedia(constraints);
            let remoteVideo = document.querySelector("#remote-video") as HTMLMediaElement;
            let localVideo = document.querySelector("#local-video") as HTMLMediaElement;
            videoText = "Getting video...";
            localVideo.srcObject = stream;
            localVideo.play();
            videoText = "Playing video";
            //Join the video call
            joinCall(callId, stream, (track: MediaStreamTrack, streams: readonly MediaStream[]) =>{
                track.onunmute = () =>{
                    if(remoteVideo) return;
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

{#await promise}
    <main>
        <p>Starting call...</p>
    </main>
{:then callData}
    <main>
        <aside>
            <div id="call-info">
                <h3>Outro Boy</h3>
            </div>
            <video id="remote-video" kind="captions" src=""></video>
            <p>{videoText}</p>
        </aside>
        <aside>
            <h3> Dono da chamada: {JSON.parse(callData).user} </h3>
            <video id="local-video" kind="captions" src=""></video>
        </aside>
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
        box-sizing: border-box;
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
