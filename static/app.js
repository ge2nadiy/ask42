new Vue({
    el: '#app',
    data: {
        formsData: [],
    },
    mounted() {
        this.getInput();
    },
    methods: {
        getInput()
        {
            const vm = this;
            axios.get('/api/input/').then(function (response) {
            console.log(response.data)
            vm.formsData = response.data
            })
        },
        addInput()
        {
            axios.post('/api/input/', {
            data: "name" + (this.formsData.length + 1),
                })
            .then(response => {
                this.getInput();
                console.log(response.data)
            })
            .catch(error => console.log(error));
        }
    }

})