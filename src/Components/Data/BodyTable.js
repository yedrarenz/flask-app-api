
import MUIDataTable from "mui-datatables";
import {Button, Container, Grid, TextField, Typography} from "@material-ui/core";
import axios from "axios";
import {useEffect, useState} from "react";
import SearchIcon from '@material-ui/icons/Search';

function BodyTable() {
    const baseUrl = 'http://localhost:5000'
    const columns = ["ID", "Name", "Team", " -- "];


    const [userData, setUserData] = useState([])

    const options = {
        filterType: 'checkbox',
    };

    useEffect(() => {
        axios.get(baseUrl + '/api/v1.0/users')
            .then((response) => {
                let i;
                let responseData = response.data
                let parsedData = []
                for (i = 0; i < responseData.length; i++) {
                    let temp = [responseData[i].id, responseData[i].name, responseData[i].team]
                    parsedData.push(temp)

                    console.log(parsedData)
                }
                setUserData(parsedData)
                // setUserData(response.data[0])
            })
    }, [])


    return (
        <Container fixed style={{marginTop: '5%'}}>
            <MUIDataTable
                title={"Employee List"}
                data={userData}
                columns={columns}
                options={options}
            />
            <Grid container justify="center" style={{marginTop: '5%'}}>
                <Grid item xs={12} justify="center">
                    <Typography align='center'>
                        <Button
                            color='primary'
                            size='large'
                            type='submit'
                            variant='contained'
                        >
                            <SearchIcon />
                            Search User by ID
                        </Button>
                    </Typography>

                </Grid>
            </Grid>
        </Container>
    )
}

export default BodyTable