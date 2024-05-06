import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditVolunteerComponent } from './edit-volunteer.component';

describe('CreateVolunteerComponent', () => {
  let component: EditVolunteerComponent;
  let fixture: ComponentFixture<EditVolunteerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditVolunteerComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EditVolunteerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
