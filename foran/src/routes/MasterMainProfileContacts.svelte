<script lang="typescript">
    import HomeLayout from "../components/HomeLayout.svelte";
    import TeacherInfo from "../components/MasterIndex.svelte";
    import Register from "../components/register/RegisterInput.svelte";
    import Button from "../components/register/RegisterButton.svelte";

</script>
    <HomeLayout>
        <div class="main-sector">
            <div class="first-sector">
                <div class="first-div">
                    <TeacherInfo name="Migue Voa"/>
                </div>
                <div class="second-div">
                    <div class="grid">
                        <Register label=Email></Register>
                        <Register label=Contacto></Register>
                        <Register label=Palavra-passe></Register>
                        <Register label="Repetir a palavra-passe"></Register>
                    </div>
                </div>
                <div class="third-div">

                </div>
            </div>
            <div class="second-sector">
                <div>
                </div>
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
    }

    .second-sector{
        width: 25%;
        height: 100%;
        display: flex;
    }

    .first-div{
        width: 100%;
        height: 30%;
        display: flex;
    }

    .second-div{
        width: 100%;
        height: 40%;
        display: flex;
    }

    .grid{
        width: 90%;
        height: 70%;
        display: flex;
        flex-wrap: wrap;
        margin: auto;
        gap: 6em;
        justify-content: center;
    }

    .third-div{
        width: 100%;
        height: 30%;
    }


</style>