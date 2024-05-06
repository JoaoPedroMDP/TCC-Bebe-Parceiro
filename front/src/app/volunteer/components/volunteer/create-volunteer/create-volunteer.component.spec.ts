import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateVolunteerComponent } from './create-volunteer.component';

describe('CreateVolunteerComponent', () => {
  let component: CreateVolunteerComponent;
  let fixture: ComponentFixture<CreateVolunteerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreateVolunteerComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CreateVolunteerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
