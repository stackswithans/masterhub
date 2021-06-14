<script lang="typescript">
    import HomeLayout from "../components/HomeLayout.svelte";

</script>

    <HomeLayout>
        <div class="main-sector">
            <div class="first-sector">
                <div class="master-camera">
                    <img src="" alt="">
                    <div class="subject">
                        <div class="time"><h4 class="h41">1:00:39</h4></div>
                        <div class="summary"><h4 class="h42">Aula</h4></div>
                    </div>
                    <div class="classroom-options">
                        <i class="fas fa-microphone fa-lg"></i>
                        <i class="fas fa-volume-up fa-lg"></i>
                        <i class="fas fa-phone-alt fa-lg"></i>
                    </div>
                </div>
                <div class="student-camera"></div>
            </div>
            <div class="second-sector">
                <img src="" alt="">
                <h3>Mais features na próxima versão. <br>Boas Aulas</h3>
            </div>
        </div>
    </HomeLayout>

<style>

    .main-sector{
        width: 100%;
        height: 93vh;
        display: flex;
    }

    .first-sector{
        width: 75%;
        height: 100%;
        display: flex;
        flex-direction: column;
        border-right: 2px solid white;
    }

    .second-sector{
        width: 25%;
        height: 100%;
        display: flex;
        align-items: center;
        text-align: center;
    }

    .master-camera{
        border-radius: 4px;
        border: 1px solid black;
        width: 100%;
        height: 65%;
    }

    .subject{
        display: flex;
        width: 20%;
        float: right;
    }

    .h41{
        margin: auto;
        color: var(--color-7);
    }

    .h42{
        margin: auto;
        color: var(--color-3);
    }

    .time{
        display: flex;
        width: 50%;
        background-color: var(--color-3);
        padding: 0.4em 0;
    }

    .summary{
        display: flex;
        width: 50%;
        background-color: var(--color-1);
        padding: 0.4em 0;
    }

    .classroom-options{
        position: relative;
        display: flex;
        gap: 2em;
        bottom: -24em;
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

    .student-camera{
        margin: auto;
        width: 20%;
        height: 20%;
        border-radius: 10px;
        border: 1px solid black;
    }

    .second-sector h3{
        margin: auto;
        opacity: 0.3;
    }

</style>