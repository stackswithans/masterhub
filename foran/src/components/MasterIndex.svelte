<script lang="typescript">
    export let name = "Maria Hill";
    export let classes = "Chemistry, Mathematics";
</script>

<div class="main">
    <div class="media">
        <div class="photo-org">
            <div class="photo">
                <img src="" alt="">
            </div>
            <div class="edit">Editar foto</div>
        </div>
    </div>
    <div class="id-div">
        <div class="identification">
            <h1>{name}</h1>
            <h2>{classes}</h2>
        </div>
    </div>
    <div class="info">
        <div>Informações pessoais</div>
        <div>Agenda</div>
        <div>Contactos</div>
        <div>Aulas</div>
    </div>
</div>



<style>
    .main{
        width: 90%;
        height: 80%;
        background-color: rgb(60, 60, 60);
        display: flex;
        border-radius: 20px;
        margin: auto;
    }

    .media{
        width: 20%;
        height: 100%;
    }

    .photo{
        width: 5em;
        height: 5em;
        border: 1px solid black;
        border-radius: 100%;
    }

    .photo-org{
        float: right;
        margin-top: 15%;
    }

    .edit{
        text-align: center;
        font-size: 0.8em;
        color: white;
    }

    .id-div{
        width: 28%;
        height: 100%;
    }

    .identification{
        margin-top: 18%;
    }

    .identification h1{
        padding-left: 0.6em;
        font-size: 1.5em;
        color: white;
    }

    .identification h2{
        padding-left: 1em;
        font-size: 1em;
        color: white;
    }

    .info{
        position: relative;
        display: flex;
        bottom: -70%;
    }

    .info div{
        padding: 0.5em 1em;
        font-size: 0.8em;
        text-align: center;
        color: white;
    }

    .info div:hover{
        border-bottom: 2px solid white;
    }


</style>