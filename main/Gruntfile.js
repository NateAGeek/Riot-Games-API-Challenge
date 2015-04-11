module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    // Task configuration.
    less: {
      development: {
        options: {
          sourceMap: true,
          sourceMapFilename: "css/main.css.map",
          sourceMapURL: "css/main.css.map",
          sourceMapBasepath: "less/",
          sourceMapRootpath: "",
        },
        files: {
          "css/style.css": "less/style.less"
        }
      }
    },
    watch: {
      styles: {
        files: [ 'less/**/*.less' ],
        tasks: [ 'less' ],
        options: {
          spawn: false,
          livereload: true
        }
      }
    }
  });

  // These plugins provide necessary tasks.
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-less');

  grunt.registerTask('default', ['development']);
  grunt.registerTask('development', ['less']);

};
