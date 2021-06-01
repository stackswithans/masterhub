<div class="form-layout">
    <slot></slot>
</div>

<style>
    .form-layout{
        display: flex;
        font-size: 16px;
        width: 55.5em; /*width-height ratio: 0.49*/
        height: 27.195em;
    }

    @media(max-width: 1300px){
        .form-layout{
            font-size: 13px;
        }
    }

    @media(max-width: 1188px){
        .form-layout{
            font-size: 11px;
        }
    }
</style>
