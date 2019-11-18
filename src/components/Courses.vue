<template>
	<v-container style="margin-top: 60px;">
		<h1>Курсы</h1>

		<v-container>
			<v-row justify="start" align="start">
				<v-col md="3" v-for="course in courses" :key="course.id">
					<!-- {{ course }} -->
					<v-card outlined>
						<v-list-item three-line>
							<v-list-item-content>
								<div class="overline mb-4">{{ course.created}}</div>
								<v-list-item-title class="headline mb-1">{{ course.name }}</v-list-item-title>
								<v-list-item-subtitle>{{ course.description }}</v-list-item-subtitle>
								<v-list-item-subtitle>Уровень: {{ course.level }}</v-list-item-subtitle>
								<v-list-item-subtitle>Дата начала: {{ course.date_start }}</v-list-item-subtitle>
								<v-list-item-subtitle>Кол-во участников: {{ course.members.length }}</v-list-item-subtitle>
							</v-list-item-content>

							<v-list-item-avatar tile size="80" color="grey"></v-list-item-avatar>
						</v-list-item>

						<v-card-actions>
							<v-btn text>Подробнее</v-btn>
						</v-card-actions>
					</v-card>
				</v-col>
			</v-row>
		</v-container>
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
