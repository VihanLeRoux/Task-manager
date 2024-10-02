document.addEventListener('DOMContentLoaded', function() {
    new Vue({
        el: '#app',
        data: {
            tasks: []
        },
        methods: {
            formatDate(dateStr) {
                const date = new Date(dateStr);
                return date.toLocaleString();
            }
        },
        mounted() {
            fetch('/api/tasks/')
                .then(response => response.json())
                .then(data => {
                    this.tasks = data.results ? data.results : data;
                })
                .catch(error => {
                    console.error('Error fetching tasks:', error);
                });
        }
    });
});
