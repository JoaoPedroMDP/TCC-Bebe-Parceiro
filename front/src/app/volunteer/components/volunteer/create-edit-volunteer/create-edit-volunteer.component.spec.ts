import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateEditVolunteerComponent } from './create-edit-volunteer.component';

describe('CreateVolunteerComponent', () => {
  let component: CreateEditVolunteerComponent;
  let fixture: ComponentFixture<CreateEditVolunteerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreateEditVolunteerComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CreateEditVolunteerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
