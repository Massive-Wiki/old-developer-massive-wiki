var index = elasticlunr(function () {
    this.setRef('id');
    this.addField('title');
    this.addField('body');
  });


