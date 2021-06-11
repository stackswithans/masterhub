<script lang="typescript">
    export let name = "Voa";
    export let course = "Física";

</script>

<div class="main">
    <div class="first">
        <div class="image">
            <img src="" alt="">
        </div>
        <div class="status"></div>
    </div>
    <div class="second">
        <div>
            <h3 class="name">{name}</h3>
            <h3 class="course">{course}</h3>
        </div>
    </div>
    <div class="third">
        <div class="icon">
            <i class="fas fa-video fa-2x"></i>
        </div>
    </div>
</div>

<style>
    .main{
        display: flex;
        width: 20rem;
        height: 6rem;
        border-bottom: 1px solid black;
    }

    .first{
        width: 6rem;
        height: 100%;
        padding: 0.8rem;
    }

    .image{
        width: 4rem;
        height: 4rem;
        border: 1px solid black;
        border-radius: 40px;
        margin: auto;
    }

    .status{
        width: 1rem;
        height: 1rem;
        border: 1px solid black;
        border-radius: 40px;
        background-color: var(--color-1);
        float: right;
        margin-top: -1rem;
    }

    .second{
        width: 9rem;
        height: 100%;
        padding: 1rem 0.5rem;
    }

    .name{
        font-size: 1.2rem;
        font-family: 'Roboto';
        color: var(--color-3);
        padding: 0.4rem 0rem;
    }

    .course{
        font-size: 1.2rem;
        font-family: 'Roboto';
        font-weight: bold;
        color: var(--color-3);
    }

    .third{
        width: 5rem;
        height: 100%;
    }
    
    .fas{
        padding: 2rem 1.4rem;
    }


</style>