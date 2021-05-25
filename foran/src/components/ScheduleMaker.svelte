<script lang="typescript">
    import { onMount } from "svelte";

    //A matrix of boolean that maps to the schedule table
    //True indicates that a time slot has been selected
    //Each time slot is an hour long
    let schedule: Array<Array<boolean>> = new Array(24); //Time slots
    for(let i = 0; i < 24; i++)
        schedule[i] = [false, false, false, false, false, false, false];//Weekdays

    const selectTimeSlot = (event) => {
        let cell: HTMLTableCellElement = event.target;
        let row: number = cell.closest("tr").rowIndex;
        let col: number = cell.cellIndex;
        //col - 1 because of the time interval col
        let slotFilled = schedule[row][col - 1];
        console.log(row + " " + col);
        console.log(slotFilled);
        slotFilled = schedule[row][col - 1] = !slotFilled;
        if(slotFilled){
            cell.style.backgroundColor = "var(--color-2)";
        }
        else{
            cell.style.backgroundColor = "var(--color-8)";
        }
    }




</script>

<table>
    <th></th>
    <th>Dom</th>
    <th>Seg</th>
    <th>Ter</th>
    <th>Quar</th>
    <th>Qui</th>
    <th>Sex</th>
    <th>Sab</th>
    {#each schedule as row, i}
        <tr class="row">
            <td>{i}:00</td>
            {#each row as _}
                <td on:click={selectTimeSlot}></td>
            {/each}
        </tr>
    {/each}
</table>

<style>
    table, tr{
        width: 60%;
    }
    
    table{
        border-radius: 2rem;
    }

    td:first-child{
        padding-right: 1%;
        text-align: end;
        vertical-align: text-top;
        width: 2rem; 
        font-size: 1rem;
    }


    td:not(:first-child){
        background-color: var(--color-8);
        width: 3.68rem;
        height: 1.75rem;

    }

    td:not(:first-child):hover{
        background-color: var(--color-2);
    }

    .row:first-of-type td:nth-child(2){
        border-top-left-radius: 0.5rem;
    }

    .row:first-of-type td:last-child{
        border-top-right-radius: 0.5rem;
    }

    .row:last-of-type td:nth-child(2){
        border-bottom-left-radius: 0.5rem;
    }

    .row:last-of-type td:last-child{
        border-bottom-right-radius: 0.5rem;
    }



</style>
