from taskmanager import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)

    # - Refers to the Task model to create a one to many relationship.
    # - Use category.tasks to get all tasks particular category
    # - Backref attr adds a category attribute to the Task class;
    #   this new attribute allows you to access the Category object
    #   associated with a specific Task object directly.
    # - lazy=True means that when we query the database for categories,
    #   it can simultaneously identify any task linked to the categories
    tasks = db.relationship("Task", backref="category",
                            cascade="all, delete", lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'category_name': self.category_name
        }


def __repr__(self):
    return self.category_name


class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=True)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=True)
    # one to many relationship with Category. A category can have many tasks
    # and when a category is deleted, all tasks associated with it are deleted
    category_id = db.Column(db.Integer, db.ForeignKey(
        "category.id", ondelete="CASCADE"),
        nullable=False)

    def __repr__(self):
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )

    def to_dict(self):
        return {
            'id': self.id,
            'task_name': self.task_name
        }
