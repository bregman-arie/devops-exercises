def removeOldBuilds(buildDirectory, days = 14) {

  def wp = new File("${buildDirectory}")
  def currentTime = new Date()
  def backTime = currentTime - days

  wp.list().each { fileName ->
      folder = new File("${buildDirectory}/${fileName}")
      if (folder.isDirectory()) {
          def timeStamp = new Date(folder.lastModified())
          if (timeStamp.before(backTime)) {
            folder.delete()
          }
      }
  }
}
