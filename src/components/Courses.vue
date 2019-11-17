<template>
	<v-container style="margin-top: 60px;">
		<h1>Курсы</h1>
		<div v-for="course in courses" :key="course.id">
			{{ course }}
		</div>
	</v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
	name: "Courses",
	data() {
		return {
			subject: "",
			msgBody: ""
		};
	},
	computed: mapState({
		courses: state => state.courses.courses
	}),
	methods: mapActions("courses", ["addCourse", "deleteCourse"]),
	created() {
		this.$store.dispatch("courses/getCourses");
		console.log(this.courses);
	}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
hr {
	max-width: 65%;
}

.msg {
	margin: 0 auto;
	max-width: 30%;
	text-align: left;
	border-bottom: 1px solid #ccc;
	padding: 1rem;
}

.msg-index {
	color: #ccc;
	font-size: 0.8rem;
	/* margin-bottom: 0; */
}

img {
	width: 250px;
	padding-top: 50px;
	padding-bottom: 50px;
}
</style>
