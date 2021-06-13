import {AppBar, makeStyles, Toolbar, Typography} from "@material-ui/core";


const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    menuButton: {
        marginRight: theme.spacing(2),
    },
    title: {
        flexGrow: 1,
    },
}));

function Header() {
    const classes = useStyles()
    return (

        <AppBar position="absolute">
            <Toolbar>
                <Typography variant="h6" className={classes.title}>
                    Test API - Renzy
                </Typography>
            </Toolbar>
        </AppBar>
    )
}

export default Header