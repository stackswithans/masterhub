<script lang="typescript">
    export let name = "Tony";
    export let course = "BI";
    export let payment = 2000;
</script>

<div class="card">
    <div class="photo-div">
        <div class="photo">
            <img src="" alt="">
        </div>
    </div>
    <div class="info-div">
        <h3 class="name">{name}</h3>
        <h3 class="course">{course}</h3>
        <h4>{payment} Kz/h</h4>
        <div class="week-days">
            <div>D</div>
            <div class="workweek">S</div>
            <div class="workweek">T</div>
            <div class="workweek">Q</div>
            <div class="workweek">Q</div>
            <div class="workweek">S</div>
            <div>S</div>
        </div>
    </div>
    <div class="icon-div">
        <div class="icon">
            <i class="fas fa-user-plus fa-lg"></i>
        </div>
    </div> 
</div>


<style>
    .card{
        width: 35%;
        height: 13vh;
        border-radius: 20px;
        display: flex;
        box-shadow: 0rem 0rem 1rem -0.3rem;
        padding: 0.6rem 0 0 0;
        background-color: white;
    }

    .photo-div{
        width: 25%;
        height: 100%;
    }

    .photo{
        border: 1px solid black;
        border-radius: 40px;
        width: 4rem;
        height: 4rem;
        float: right;
    }

    .info-div{
        width: 60%;
        height: 100%;
        display: flex;
        flex-direction: column;
        padding: 0rem 0.5rem;
    }

    .week-days{
        display: flex;
        gap: 8%;
        padding: 0.4rem 0;
    }

    .week-days div{
        font-family: 'Roboto Slab';
        font-size: 1.2rem;
    }

    .workweek{
        color: var(--color-1);
    }

    .icon-div{
        height: 100%;
        width: 15%;
        display: flex;
        align-items: center;
    }

    .icon{
        margin: auto;
    }

    .name{
        font-size: 'Roboto';
        color: var(--color-3);
        font-size: 1.2rem;
        padding-top: 0.2rem
    }

    .course{
        font-size: 'Roboto Bold';
        color: var(--color-3);
        font-size: 1.2rem;
        padding-top: 0.2;
    }

    h4{
        font-family: 'Roboto Condensed';
        color: var(--color-1);
    }

    

</style>